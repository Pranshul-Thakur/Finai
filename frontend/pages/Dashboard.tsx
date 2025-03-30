import React from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { MessageSquare, LineChart, BookOpen, Briefcase, ArrowRight } from 'lucide-react';

const cards = [
  {
    title: 'AI Assistant',
    description: 'Get personalized financial advice and answers to your investment queries',
    icon: MessageSquare,
    color: 'bg-gradient-to-br from-blue-500 to-blue-600',
    path: '/chatbot'
  },
  {
    title: 'Market Analytics',
    description: 'Track market trends and analyze stock performance',
    icon: LineChart,
    color: 'bg-gradient-to-br from-purple-500 to-purple-600',
    path: '/analytics'
  },
  {
    title: 'Investment Guide',
    description: 'Learn investment basics and advanced strategies',
    icon: BookOpen,
    color: 'bg-gradient-to-br from-green-500 to-green-600',
    path: '/guide'
  },
  {
    title: 'Portfolio Manager',
    description: 'Track and manage your investment portfolio',
    icon: Briefcase,
    color: 'bg-gradient-to-br from-orange-500 to-orange-600',
    path: '/portfolio'
  }
];

export default function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-12 text-center"
        >
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-purple-500 text-transparent bg-clip-text">
            FinAI Assistant
          </h1>
          <p className="text-gray-400 text-xl">Your intelligent financial companion</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {cards.map((card, index) => (
            <motion.div
              key={card.title}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`${card.color} rounded-2xl p-1`}
            >
              <div className="bg-gray-800 rounded-xl p-6 h-full transform transition-transform hover:scale-[1.02]">
                <div className="flex items-start justify-between">
                  <card.icon size={32} className="text-white" />
                  <ArrowRight size={24} className="text-gray-400" />
                </div>
                <h2 className="text-2xl font-semibold mt-4 mb-2">{card.title}</h2>
                <p className="text-gray-400 mb-4">{card.description}</p>
                <button
                  onClick={() => navigate(card.path)}
                  className="mt-4 px-6 py-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
                >
                  Explore
                </button>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}