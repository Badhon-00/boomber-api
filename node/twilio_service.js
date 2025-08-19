const twilio = require('twilio');
const client = twilio(
  process.env.TWILIO_SID,
  process.env.TWILIO_AUTH_TOKEN
);

module.exports = {
  sendSMS: (to, message) => {
    return client.messages.create({
      body: message,
      from: process.env.TWILIO_PHONE_NUMBER,
      to: to
    });
  }
};