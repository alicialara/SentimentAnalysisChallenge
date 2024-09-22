import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header';
import SentimentForm from './SentimentForm';
import './App.css';

function App() {
  const [result, setResult] = useState(null);

  const handleSubmit = async (text) => {
    try {
      const response = await axios.post('http://0.0.0.0:5000/analyze', { text });
      console.log(response.data);
      setResult(response.data);
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
    }
  };

  return (
    <div className="App">
      <Header />
      <main>
        <section id="input-section">
          <h2>Analyze Sentiment</h2>
          <SentimentForm onSubmit={handleSubmit} />
        </section>
        <section id="result-section">
          <h2>Result</h2>
          {result && (
            <div id="result">
  <p>Label: {result.label}</p>
  <p>Score: {result.score}</p>
  <div className="sentiment-bar">
    <div
      className="sentiment-bar-fill"
      style={{ width: `${result.score * 100}%`, backgroundColor: result.score > 0.5 ? 'green' : 'red' }}
    ></div>
  </div>
  <p>Timestamp: {result.timestamp}</p>
</div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
