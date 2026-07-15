const CONFIG = {
  projectId: "belajaronline-b5512",
  apiKey: "AIzaSyAkX8qAS-O_5m_qaGr8Aa9XME-lVyBMibw",
  appId: "belajaronline-b5512"
};

function getFirebaseAuthToken() {
  const url = `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=${CONFIG.apiKey}`;
  const response = UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({ returnSecureToken: true }),
    muteHttpExceptions: true
  });
  return JSON.parse(response.getContentText()).idToken; 
}

// ----------------------------------------------------
// FUNGSI MAPPING SUPER LENGKAP UNTUK FIRESTORE
// Mendukung Teks, Angka, Boolean, Array, dan Object!
// ----------------------------------------------------
function mapToFirestoreValue(value) {
  if (value === null || value === undefined) return { nullValue: null };
  const type = typeof value;
  if (type === "string") return { stringValue: value };
  if (type === "number") {
    if (Number.isInteger(value)) return { integerValue: value };
    return { doubleValue: value };
  }
  if (type === "boolean") return { booleanValue: value };
  if (Array.isArray(value)) {
    return { arrayValue: { values: value.map(v => mapToFirestoreValue(v)) } };
  }
  if (type === "object") {
    const fields = {};
    for (let key in value) {
      if (value[key] !== undefined) {
        fields[key] = mapToFirestoreValue(value[key]);
      }
    }
    return { mapValue: { fields: fields } };
  }
  return { nullValue: null };
}

function mapToFirestoreDoc(obj) {
  const fields = {};
  for (let key in obj) {
    if (obj[key] !== undefined) {
      fields[key] = mapToFirestoreValue(obj[key]);
    }
  }
  return { fields: fields };
}

function mapFromFirestoreValue(valObj) {
  if (!valObj) return null;
  if (valObj.stringValue !== undefined) return valObj.stringValue;
  if (valObj.integerValue !== undefined) return parseInt(valObj.integerValue);
  if (valObj.doubleValue !== undefined) return parseFloat(valObj.doubleValue);
  if (valObj.booleanValue !== undefined) return valObj.booleanValue;
  if (valObj.nullValue !== undefined) return null;
  if (valObj.arrayValue !== undefined) {
    return (valObj.arrayValue.values || []).map(v => mapFromFirestoreValue(v));
  }
  if (valObj.mapValue !== undefined) {
    const obj = {};
    const fields = valObj.mapValue.fields || {};
    for (let key in fields) {
      obj[key] = mapFromFirestoreValue(fields[key]);
    }
    return obj;
  }
  return null;
}

function mapFromFirestoreDoc(doc) {
  const obj = {};
  if (!doc.fields) return obj;
  for (let key in doc.fields) {
    obj[key] = mapFromFirestoreValue(doc.fields[key]);
  }
  return obj;
}
// ----------------------------------------------------

function doPost(e) {
  try {
    const postData = JSON.parse(e.postData.contents);
    const action = postData.action;

    
    // --- FITUR VERIFIKASI PIN ---
    if (action === 'verifyPin') {
      if (postData.pin === '443588') {
        return ContentService.createTextOutput(JSON.stringify({ status: 'success' })).setMimeType(ContentService.MimeType.JSON);
      } else {
        return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: 'PIN Salah!' })).setMimeType(ContentService.MimeType.JSON);
      }
    }
    // --- FITUR LOGIN ADMIN ---
    if (action === "login") {
      const username = postData.username;
      const password = postData.password;
      
      if (username === "ahmad_zulfikar" && password === "naylis&zulfi2019") {
        return ContentService.createTextOutput(JSON.stringify({ 
          status: "success", token: "admin_token_mtsn6_live" 
        })).setMimeType(ContentService.MimeType.JSON);
      } else {
        return ContentService.createTextOutput(JSON.stringify({ 
          status: "error", message: "Username atau Password salah!" 
        })).setMimeType(ContentService.MimeType.JSON);
      }
    }

    const token = getFirebaseAuthToken();
    let baseUrl = `https://firestore.googleapis.com/v1/projects/${CONFIG.projectId}/databases/(default)/documents/${postData.path}`;

    if (action === "addDoc") {
      const docData = mapToFirestoreDoc(postData.data);
      const res = UrlFetchApp.fetch(baseUrl, {
        method: "post",
        contentType: "application/json",
        headers: { "Authorization": "Bearer " + token },
        payload: JSON.stringify(docData),
        muteHttpExceptions: true
      });
      const resJson = JSON.parse(res.getContentText());
      if (resJson.error) throw new Error(resJson.error.message);
      
      const docId = resJson.name.split("/").pop();
      return ContentService.createTextOutput(JSON.stringify({ status: "success", id: docId })).setMimeType(ContentService.MimeType.JSON);
    }
    
    if (action === "setDoc" || action === "updateDoc") {
      if (action === "updateDoc") {
          baseUrl += `?updateMask.fieldPaths=${Object.keys(postData.data).join("&updateMask.fieldPaths=")}`;
      }
      const docData = mapToFirestoreDoc(postData.data);
      const res = UrlFetchApp.fetch(baseUrl, {
        method: "patch",
        contentType: "application/json",
        headers: { "Authorization": "Bearer " + token },
        payload: JSON.stringify(docData),
        muteHttpExceptions: true
      });
      const resJson = JSON.parse(res.getContentText());
      if (resJson.error) throw new Error(resJson.error.message);
      
      return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);
    }

    if (action === "deleteDoc") {
      const res = UrlFetchApp.fetch(baseUrl, {
        method: "delete",
        headers: { "Authorization": "Bearer " + token },
        muteHttpExceptions: true
      });
      return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);
    }
    
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Unknown action" })).setMimeType(ContentService.MimeType.JSON);

  } catch(err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  try {
    const action = e.parameter.action;
    const path = e.parameter.path;
    
    if (!action || !path) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Missing action or path" })).setMimeType(ContentService.MimeType.JSON);
    }

    const token = getFirebaseAuthToken();
    let baseUrl = `https://firestore.googleapis.com/v1/projects/${CONFIG.projectId}/databases/(default)/documents/${path}`;

    if (action === "getDocs") {
      baseUrl += `?pageSize=300`;
      const res = UrlFetchApp.fetch(baseUrl, {
        method: "get",
        headers: { "Authorization": "Bearer " + token },
        muteHttpExceptions: true
      });
      const resJson = JSON.parse(res.getContentText());
      if (resJson.error) throw new Error(resJson.error.message);
      
      const docs = (resJson.documents || []).map(doc => {
        return {
          id: doc.name.split("/").pop(),
          fields: mapFromFirestoreDoc(doc)
        };
      });
      
      return ContentService.createTextOutput(JSON.stringify({ status: "success", data: docs })).setMimeType(ContentService.MimeType.JSON);
    }
    
    if (action === "getDoc") {
      const res = UrlFetchApp.fetch(baseUrl, {
        method: "get",
        headers: { "Authorization": "Bearer " + token },
        muteHttpExceptions: true
      });
      const resJson = JSON.parse(res.getContentText());
      if (resJson.error) {
        if(resJson.error.code === 404) return ContentService.createTextOutput(JSON.stringify({ status: "success", data: {} })).setMimeType(ContentService.MimeType.JSON);
        throw new Error(resJson.error.message);
      }
      
      const doc = {
        id: resJson.name.split("/").pop(),
        fields: mapFromFirestoreDoc(resJson)
      };
      
      return ContentService.createTextOutput(JSON.stringify({ status: "success", data: doc })).setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Unknown GET action" })).setMimeType(ContentService.MimeType.JSON);

  } catch(err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}