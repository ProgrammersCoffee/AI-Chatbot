import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    {
      role: "assistant",
      text: "Hello. How can I assist you today?",
    },
  ]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      text: message,
    };

    setChat((prev) => [...prev, userMessage]);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          role: "user",
          message: message,
        }),
      });

      const data = await res.json();

      // اطبع الرد في Console
      console.log("Backend Response:", data);

      // احتمالات مختلفة للرد
      const botResponse =
        data.response ||
        data.message ||
        data.content ||
        "No response from backend";

      setChat((prev) => [
        ...prev,
        {
          role: "assistant",
          text: botResponse,
        },
      ]);
    } catch (error) {
      console.error("Error:", error);

      setChat((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Backend connection error",
        },
      ]);
    }

    setMessage("");
  };

  return (
    <div className="app">
      <div className="chat-container">
        <h1>AI Chatbot</h1>

        <div className="chat-box">
          {chat.map((msg, index) => (
            <div
              key={index}
              className={`message ${
                msg.role === "user" ? "user" : "bot"
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
          />

          <button onClick={sendMessage}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;