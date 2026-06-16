const GAS_URL = "https://script.google.com/macros/s/AKfycbwJ5xTkkYn8CuWU2cax8NdlkKXCMn5uCOy_68FaVJxXvFhFw9qu6ihCl4hvan7FpZ5niA/exec";

export function initializeApp(config) { return {}; }
export function getAuth() { return { currentUser: { uid: "anonymous-user" } }; }
export async function signInAnonymously(auth) { return { user: auth.currentUser }; }
export function onAuthStateChanged(auth, cb) { cb(auth.currentUser); }
export function getFirestore(app) { return {}; }
export function collection(db, ...paths) { return paths.join('/'); }
export function doc(db, ...paths) { return paths.join('/'); }
export function query(col, ...args) { 
    let q = { path: col };
    args.forEach(arg => { if (arg && arg.type === 'orderBy') q.orderBy = arg; });
    return q;
}
export function orderBy(field, dir) { return { type: 'orderBy', field, dir }; }
export function limit(n) { return { type: 'limit', n }; }

function serializeData(data) {
    let result = {};
    for (let key in data) {
        if (data[key] === null || data[key] === undefined) continue;
        if (typeof data[key] === 'object') {
            result[key] = JSON.stringify(data[key]);
        } else {
            result[key] = data[key];
        }
    }
    return result;
}

function deserializeData(data) {
    let result = {};
    for (let key in data) {
        if (typeof data[key] === 'string' && (data[key].startsWith('[') || data[key].startsWith('{'))) {
            try {
                result[key] = JSON.parse(data[key]);
            } catch(e) {
                result[key] = data[key];
            }
        } else {
            result[key] = data[key];
        }
    }
    return result;
}

export async function addDoc(colPath, data) {
    const res = await fetch(GAS_URL, {
        method: "POST",
        headers: {"Content-Type": "text/plain"},
        body: JSON.stringify({ action: "addDoc", path: colPath, data: serializeData(data) })
    });
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
    return { id: result.id };
}

export async function setDoc(docPath, data) {
    const res = await fetch(GAS_URL, {
        method: "POST",
        headers: {"Content-Type": "text/plain"},
        body: JSON.stringify({ action: "setDoc", path: docPath, data: serializeData(data) })
    });
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
}

export async function updateDoc(docPath, data) {
    const res = await fetch(GAS_URL, {
        method: "POST",
        headers: {"Content-Type": "text/plain"},
        body: JSON.stringify({ action: "updateDoc", path: docPath, data: serializeData(data) })
    });
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
}

export async function deleteDoc(docPath) {
    const res = await fetch(GAS_URL, {
        method: "POST",
        headers: {"Content-Type": "text/plain"},
        body: JSON.stringify({ action: "deleteDoc", path: docPath })
    });
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
}

export async function getDocs(queryObj) {
    const colPath = typeof queryObj === 'string' ? queryObj : queryObj.path || queryObj; 
    const res = await fetch(`${GAS_URL}?action=getDocs&path=${encodeURIComponent(colPath)}`);
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
    
    let rawDocs = result.data || [];
    if (queryObj.orderBy) {
        rawDocs.sort((a, b) => {
            let valA = a.fields[queryObj.orderBy.field];
            let valB = b.fields[queryObj.orderBy.field];
            if (valA < valB) return queryObj.orderBy.dir === 'desc' ? 1 : -1;
            if (valA > valB) return queryObj.orderBy.dir === 'desc' ? -1 : 1;
            return 0;
        });
    }

    const docs = rawDocs.map(d => ({
        id: d.id,
        data: () => deserializeData(d.fields)
    }));
    return { empty: docs.length === 0, docs: docs, forEach: (cb) => docs.forEach(cb) };
}

export async function getDoc(queryObj) {
    const docPath = typeof queryObj === 'string' ? queryObj : queryObj.path || queryObj; 
    const res = await fetch(`${GAS_URL}?action=getDoc&path=${encodeURIComponent(docPath)}`);
    const result = await res.json();
    if(result.status !== "success") throw new Error(result.message);
    
    return {
        id: result.data.id,
        exists: () => !!result.data.fields,
        data: () => deserializeData(result.data.fields),
        metadata: { hasPendingWrites: false }
    };
}

export function onSnapshot(queryObj, callback, errorCallback) {
    let isCancelled = false;
    const pathStr = typeof queryObj === 'string' ? queryObj : queryObj.path || queryObj; 
    const isDoc = pathStr.split('/').length % 2 === 0;

    async function fetchUpdate() {
        if(isCancelled) return;
        try {
            const snapshot = isDoc ? await getDoc(queryObj) : await getDocs(queryObj);
            if(!isCancelled) callback(snapshot);
        } catch(err) {
            if(errorCallback && !isCancelled) errorCallback(err);
        }
    }
    fetchUpdate();
    const interval = setInterval(fetchUpdate, 10000); // Polling every 10s
    return () => {
        isCancelled = true;
        clearInterval(interval);
    };
}
