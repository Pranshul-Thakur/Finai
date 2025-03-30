import React from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Wallet, TrendingUp, PieChart } from 'lucide-react';

export default function PortfolioPage() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="max-w-7xl mx-auto"
      >
        <button
          onClick={() => navigate('/')}
          className="flex items-center gap-2 text-gray-400 hover:text-white mb-8 transition-colors"
        >
          <ArrowLeft size={20} />
          Back to Dashboard
        </button>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-gray-800 rounded-xl p-6"
          >
            <div className="flex items-center gap-4 mb-4">
              <Wallet className="text-blue-400" size={24} />
              <h2 className="text-2xl font-semibold">Total Portfolio Value</h2>
            </div>
            <p className="text-4xl font-bold text-blue-400">₹2,45,000</p>
            <p className="text-green-400 flex items-center gap-2 mt-2">
              <TrendingUp size={20} />
              +15.4% this month
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="bg-gray-800 rounded-xl p-6"
          >
            <div className="flex items-center gap-4 mb-4">
              <PieChart className="text-purple-400" size={24} />
              <h2 className="text-2xl font-semibold">Asset Allocation</h2>
            </div>
            <div className="space-y-4">
              <div>
                <div className="flex justify-between mb-1">
                  <span>Stocks</span>
                  <span>60%</span>
                </div>
                <div className="h-2 bg-gray-700 rounded-full">
                  <div className="h-full w-[60%] bg-blue-400 rounded-full"></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between mb-1">
                  <span>Mutual Funds</span>
                  <span>30%</span>
                </div>
                <div className="h-2 bg-gray-700 rounded-full">
                  <div className="h-full w-[30%] bg-purple-400 rounded-full"></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between mb-1">
                  <span>Fixed Deposits</span>
                  <span>10%</span>
                </div>
                <div className="h-2 bg-gray-700 rounded-full">
                  <div className="h-full w-[10%] bg-green-400 rounded-full"></div>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </motion.div>
    </div>
  );
}