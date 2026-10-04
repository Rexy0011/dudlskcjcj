const http = require('http');
const { spawn } = require('child_process');

const PORT = process.env.PORT || 8080;

// 1. Start HTTP Server for Render
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('OK');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Health check server running on port ${PORT}`);
});

// 2. Spawn your Python script (gen.py)
const pythonProcess = spawn('python', ['gen.py']); // Use 'python3' if required by your environment

pythonProcess.stdout.on('data', (data) => {
  console.log(`[gen.py]: ${data.toString()}`);
});

pythonProcess.stderr.on('data', (data) => {
  console.error(`[gen.py ERROR]: ${data.toString()}`);
});

pythonProcess.on('close', (code) => {
  console.log(`gen.py process exited with code ${code}`);
});
