import React, { useState } from 'react';
import './SentimentForm.css';

function SentimentForm({ onSubmit }) {
  const [text, setText] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(text);
  };

  return (
    <div className="SentimentForm">
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Enter text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        ></textarea>
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
}

export default SentimentForm;
