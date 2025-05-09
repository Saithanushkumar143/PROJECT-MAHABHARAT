import React, { useState } from "react";
import "./App.css";

const App = () => {
  const [query, setQuery] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://localhost:5000/get_wisdom?query=${query}`);
      const result = await response.json();

      if (response.ok) {
        setData(result);
        setError(null);
        speakOutLoud(result.lesson, result.shloka); // 🔊 Speak lesson and shloka
      } else {
        setError(result.error);
        setData(null);
      }
    } catch (error) {
      console.error("Error:", error);
      setError("Failed to fetch wisdom.");
    }
  };

  // 🔈 Voice function
  const speakOutLoud = (lesson, shloka) => {
    const utterLesson = new SpeechSynthesisUtterance(`Lesson: ${lesson}`);
    const utterShloka = new SpeechSynthesisUtterance(`Shloka: ${shloka}`);

    // Optional: Change voice or speed if needed
    utterLesson.rate = 1;
    utterShloka.rate = 1;

    window.speechSynthesis.speak(utterLesson);
    window.speechSynthesis.speak(utterShloka);
  };

  return (
    <div className="container">
      <h1>🔱 Mahabharata Wisdom 🔱</h1>
      <input
        type="text"
        placeholder="Enter query (e.g., Leadership, Friendship)..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Get Wisdom</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <div className="wisdom-card">
          <h2>📜 {data.scenario}</h2>
          <p><strong>Characters:</strong> {data.characters.join(", ")}</p>
          <p><strong>Lesson:</strong> {data.lesson}</p>
          <p className="shloka">🕉️ {data.shloka}</p>
        </div>
      )}
    </div>
  );
};

export default App;
