import React, { useState } from 'react';
import { Send, Bot } from 'lucide-react';

interface Message {
  text: string;
  isBot: boolean;
}

export default function ChatBot() {
  const [messages, setMessages] = useState<Message[]>([
    { text: "Hi! I'm your financial assistant. How can I help you today?", isBot: true }
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;
    
    setMessages(prev => [...prev, { text: input, isBot: false }]);
    // Simulated bot response
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        text: "I understand you're interested in investing. Let me help guide you through the basics.", 
        isBot: true 
      }]);
    }, 1000);
    setInput('');
  };

  return (
    <div className="h-[600px] bg-white rounded-lg shadow-lg flex flex-col">
      <div className="bg-blue-600 p-4 rounded-t-lg">
        <div className="flex items-center gap-2">
          <Bot className="text-white" size={24} />
          <h2 className="text-white text-lg font-semibold">Financial Assistant</h2>
        </div>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div key={index} className={`flex ${message.isBot ? 'justify-start' : 'justify-end'}`}>
            <div className={`max-w-[80%] p-3 rounded-lg ${
              message.isBot 
                ? 'bg-gray-100 text-gray-800' 
                : 'bg-blue-600 text-white'
            }`}>
              {message.text}
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 border-t">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Ask about investing..."
            className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSend}
            className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 transition-colors"
          >
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
}