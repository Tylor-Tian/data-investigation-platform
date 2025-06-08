import React, { useEffect, useState } from 'react';

export default function App() {
  const [status, setStatus] = useState('');

  useEffect(() => {
    fetch('/health')
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('offline'));
  }, []);

  return (
    <div>
      <h1>Data Investigation Platform</h1>
      <p>API status: {status}</p>
    </div>
  );
}
