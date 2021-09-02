import axios from 'axios';

 export async function turnOffSign() {
  let status = {};
  await axios
    .get('/api/turn-off')
    .catch(err => {
      status.responseData = err;
      status.error = true;
    });
  return status;
}

export async function healthCheck() {
  let status = {};
  await axios
    .get('/api/health-check')
    .then(({ data }) => {
      const { success, ...maybeData } = data;
      status.error = !success;
      if (maybeData.existingMessage) {
        status.message = { ...maybeData };
      }
    })
    .catch(err => {
      status.responseData = err;
      status.error = true;
    });
  return status;
}

export async function updateSignText(signData) {
  let status = {};
  await axios
    .post('/api/update-sign', { ...signData })
    .then(res => {
      status = res.data;
    })
    .catch(err => {
      status.responseData = err;
      status.error = true;
    });
  return status;
}

export async function getRandomInput() {
  let status = {};
  await axios
    .get('/api/random')
    .then(res => {
      status.responseData = res.data;
    })
    .catch(() => {
      status.error = true;
    });
  return status;
}
