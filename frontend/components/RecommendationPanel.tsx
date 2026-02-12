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

interface RecommendationPanelProps {
    result: AnalysisResult
}

export default function RecommendationPanel({ result }: RecommendationPanelProps) {
    type ConditionKey = 'diabetes' | 'heart_disease' | 'high_cholesterol'

    const conditions: { key: ConditionKey; label: string; icon: string; color: string }[] = [
        { key: 'diabetes', label: 'Diabetes', icon: '🩺', color: 'blue' },
        { key: 'heart_disease', label: 'Heart Disease', icon: '❤️', color: 'red' },
        { key: 'high_cholesterol', label: 'High Cholesterol', icon: '💊', color: 'purple' },
    ]

    const getRiskLevel = (score: number) => {
        if (score < 30) return 'low'
        if (score < 60) return 'moderate'
        return 'high'
    }

    const getPriorityBadge = (score: number) => {
        const level = getRiskLevel(score)
        if (level === 'high') return <span className="risk-badge-high">High Priority</span>
        if (level === 'moderate') return <span className="risk-badge-moderate">Medium Priority</span>
        return <span className="risk-badge-low">Low Priority</span>
    }

    return (
        <div className="card">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
                <svg className="w-7 h-7 mr-3 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                </svg>
                Personalized Recommendations
            </h2>

            <div className="space-y-6">
                {conditions.map((condition, index) => {
                    const score = result.risk_scores[condition.key] || 0
                    const recommendation = result.recommendations[condition.key]

                    // Parse recommendations into bullet points
                    const points = recommendation.split('.').filter((p: string) => p.trim().length > 0)

                    return (
                        <motion.div
                            key={condition.key}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.5, delay: index * 0.15 }}
                            className="bg-gradient-to-r from-gray-50 to-white p-5 rounded-lg border border-gray-200 hover:shadow-md transition-shadow duration-300"
                        >
                            <div className="flex items-start justify-between mb-3">
                                <div className="flex items-center">
                                    <span className="text-2xl mr-3">{condition.icon}</span>
                                    <div>
                                        <h3 className="font-semibold text-gray-800 text-lg">{condition.label}</h3>
                                        <p className="text-sm text-gray-500">Risk Score: {score.toFixed(1)}%</p>
                                    </div>
                                </div>
                                {getPriorityBadge(score)}
                            </div>

                            <div className="space-y-2">
                                {points.map((point: string, idx: number) => (
                                    <div key={idx} className="flex items-start">
                                        <svg className="w-5 h-5 text-primary-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                                        </svg>
                                        <p className="text-sm text-gray-700">{point.trim()}.</p>
                                    </div>
                                ))}
                            </div>
                        </motion.div>
                    )
                })}
            </div>

            <div className="mt-6 p-4 bg-primary-50 border-l-4 border-primary-500 rounded">
                <div className="flex items-start">
                    <svg className="w-6 h-6 text-primary-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <div>
                        <h4 className="font-semibold text-primary-900 mb-1">Important Notice</h4>
                        <p className="text-sm text-primary-800">
                            These recommendations are AI-generated based on your health data. For high-risk conditions,
                            please consult with a healthcare professional immediately. This system is for informational
                            purposes only and should not replace professional medical advice.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    )
}
