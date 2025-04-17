import React from "react";

const ThoughtSlogan = ({ thought, slogan }) => {
  const speakText = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1; // speaking rate
    utterance.pitch = 1; // voice pitch
    speechSynthesis.speak(utterance);
  };

  const handleSpeak = () => {
    const message = `Today's thought is: ${thought}. And the slogan is: ${slogan}`;
    speakText(message);
  };

  return (
    <div className="text-center mt-4">
      <h2 className="text-xl font-semibold">Thought: {thought}</h2>
      <h3 className="text-lg font-medium mt-2">Slogan: {slogan}</h3>
      <button
        onClick={handleSpeak}
        className="mt-4 bg-blue-600 hover:bg-blue-800 text-white py-2 px-4 rounded-full transition"
      >
        🔊 Speak Out
      </button>
    </div>
  );
};

export default ThoughtSlogan;
