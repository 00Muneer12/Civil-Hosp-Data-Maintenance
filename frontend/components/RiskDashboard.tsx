'use client'

import { motion } from 'framer-motion'

interface AnalysisResult {
    user_id: string
    risk_scores: {
        diabetes: number
        heart_disease: number
        high_cholesterol: number
    }
    recommendations: {
        diabetes: string
        heart_disease: string
        high_cholesterol: string
    }
    explanations: {
        diabetes: string
        heart_disease: string
        high_cholesterol: string
    }
    timestamp: string
}

interface RiskDashboardProps {
    result: AnalysisResult
}

export default function RiskDashboard({ result }: RiskDashboardProps) {
    const getRiskColor = (score: number) => {
        if (score < 30) return { bg: 'bg-green-100', text: 'text-green-800', border: 'border-green-500', fill: 'stroke-green-500' }
        if (score < 60) return { bg: 'bg-yellow-100', text: 'text-yellow-800', border: 'border-yellow-500', fill: 'stroke-yellow-500' }
        return { bg: 'bg-red-100', text: 'text-red-800', border: 'border-red-500', fill: 'stroke-red-500' }
    }

    const getRiskLevel = (score: number) => {
        if (score < 30) return 'Low Risk'
        if (score < 60) return 'Moderate Risk'
        return 'High Risk'
    }

    type ConditionKey = 'diabetes' | 'heart_disease' | 'high_cholesterol'

    const conditions: { key: ConditionKey; label: string; icon: string }[] = [
        { key: 'diabetes', label: 'Diabetes', icon: '🩺' },
        { key: 'heart_disease', label: 'Heart Disease', icon: '❤️' },
        { key: 'high_cholesterol', label: 'High Cholesterol', icon: '💊' },
    ]

    return (
        <div className="card">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
                <svg className="w-7 h-7 mr-3 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Risk Assessment
            </h2>

            <div className="space-y-6">
                {conditions.map((condition, index) => {
                    const score = result.risk_scores[condition.key] || 0
                    const colors = getRiskColor(score)
                    const riskLevel = getRiskLevel(score)

                    return (
                        <motion.div
                            key={condition.key}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: index * 0.1 }}
                            className="border-l-4 pl-4"
                            style={{ borderColor: colors.border.replace('border-', '') }}
                        >
                            <div className="flex items-center justify-between mb-3">
                                <div className="flex items-center">
                                    <span className="text-2xl mr-3">{condition.icon}</span>
                                    <div>
                                        <h3 className="font-semibold text-gray-800">{condition.label}</h3>
                                        <span className={`text-sm font-medium ${colors.text}`}>{riskLevel}</span>
                                    </div>
                                </div>
                                <div className="text-right">
                                    <div className={`text-3xl font-bold ${colors.text}`}>{score.toFixed(1)}%</div>
                                </div>
                            </div>

                            {/* Progress Bar */}
                            <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
                                <motion.div
                                    initial={{ width: 0 }}
                                    animate={{ width: `${score}%` }}
                                    transition={{ duration: 1, delay: index * 0.1 + 0.3 }}
                                    className={`h-full rounded-full bg-gradient-to-r ${score < 30
                                        ? 'from-green-400 to-green-600'
                                        : score < 60
                                            ? 'from-yellow-400 to-yellow-600'
                                            : 'from-red-400 to-red-600'
                                        }`}
                                />
                            </div>

                            {/* Explanation */}
                            <p className="text-sm text-gray-600 mt-3 italic">
                                {result.explanations[condition.key]}
                            </p>
                        </motion.div>
                    )
                })}
            </div>

            <div className="mt-6 pt-6 border-t border-gray-200">
                <p className="text-xs text-gray-500">
                    <strong>User ID:</strong> {result.user_id}
                </p>
                <p className="text-xs text-gray-500">
                    <strong>Analysis Date:</strong> {new Date(result.timestamp).toLocaleString()}
                </p>
            </div>
        </div>
    )
}
