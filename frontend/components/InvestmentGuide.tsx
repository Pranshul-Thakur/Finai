import React from 'react';
import { BookOpen, AlertTriangle, TrendingUp } from 'lucide-react';

export default function InvestmentGuide() {
  return (
    <div className="bg-white p-6 rounded-lg shadow-lg">
      <h2 className="text-xl font-semibold mb-4">Investment Guide</h2>
      <div className="space-y-4">
        <div className="flex items-start gap-3">
          <BookOpen className="text-blue-600" size={24} />
          <div>
            <h3 className="font-semibold">Basic Concepts</h3>
            <p className="text-gray-600">Learn about stocks, mutual funds, and basic investment terms.</p>
          </div>
        </div>
        
        <div className="flex items-start gap-3">
          <AlertTriangle className="text-yellow-600" size={24} />
          <div>
            <h3 className="font-semibold">Risk Assessment</h3>
            <p className="text-gray-600">Understand your risk tolerance and investment goals.</p>
          </div>
        </div>
        
        <div className="flex items-start gap-3">
          <TrendingUp className="text-green-600" size={24} />
          <div>
            <h3 className="font-semibold">Market Analysis</h3>
            <p className="text-gray-600">Get insights into market trends and analysis.</p>
          </div>
        </div>
      </div>
    </div>
  );
}