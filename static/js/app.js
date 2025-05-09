function handleSpeak() {
    const lessonText = document.getElementById("lessonText").innerText;

    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(lessonText);
        utterance.rate = 1;        // Speed (0.1 to 10)
        utterance.pitch = 1;       // Voice pitch (0 to 2)
        utterance.volume = 1;      // Volume (0 to 1)
        utterance.lang = 'en-IN';  // Indian English accent

        speechSynthesis.speak(utterance);
    } else {
        alert("Speech synthesis not supported in this browser.");
    }
}
