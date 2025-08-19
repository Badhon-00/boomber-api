require('dotenv').config();
const express = require('express');
const { sendSMS } = require('./node/twilio_service');

const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.json());

app.post('/api/sms', async (req, res) => {
  try {
    const result = await sendSMS(req.body.to, req.body.message);
    res.json({ success: true, sid: result.sid });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Boomber API running on port ${PORT}`);
});