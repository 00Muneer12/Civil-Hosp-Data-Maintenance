'use client'

import { useState } from 'react'
import HealthDataForm from '@/components/HealthDataForm'
import RiskDashboard from '@/components/RiskDashboard'
import RecommendationPanel from '@/components/RecommendationPanel'
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

export default function Home() {
    const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null)
    const [loading, setLoading] = useState(false)

    const handleAnalysisComplete = (result: AnalysisResult) => {
        setAnalysisResult(result)
    }

    return (
        <main className="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-12"
                >
                    <div className="flex items-center justify-center mb-4">
                        <div className="bg-gradient-to-r from-primary-600 to-secondary-600 p-4 rounded-2xl shadow-lg">
                            <svg className="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                            </svg>
                        </div>
                    </div>
                    <h1 className="text-5xl font-bold bg-gradient-to-r from-primary-600 to-secondary-600 bg-clip-text text-transparent mb-4">
                        HealthNexus AI
                    </h1>
                    <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                        Advanced AI-powered health risk prediction and personalized recommendations
                    </p>
                </motion.div>

                {/* Main Content */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    {/* Left Column - Input Form */}
                    <motion.div
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.6, delay: 0.2 }}
                    >
                        <HealthDataForm
                            onAnalysisComplete={handleAnalysisComplete}
                            setLoading={setLoading}
                        />
                    </motion.div>

                    {/* Right Column - Results */}
                    <motion.div
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.6, delay: 0.4 }}
                        className="space-y-8"
                    >
                        {loading ? (
                            <div className="card flex items-center justify-center h-96">
                                <div className="text-center">
                                    <div className="inline-block animate-spin rounded-full h-16 w-16 border-4 border-primary-500 border-t-transparent"></div>
                                    <p className="mt-4 text-gray-600 font-medium">Analyzing your health data...</p>
                                </div>
                            </div>
                        ) : analysisResult ? (
                            <>
                                <RiskDashboard result={analysisResult} />
                                <RecommendationPanel result={analysisResult} />
                            </>
                        ) : (
                            <div className="card flex items-center justify-center h-96 bg-gradient-to-br from-primary-50 to-secondary-50">
                                <div className="text-center">
                                    <svg className="w-24 h-24 text-blue-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                    </svg>
                                    <p className="text-gray-500 text-lg">Enter your health data to get started</p>
                                    <p className="text-gray-400 text-sm mt-2">AI-powered analysis will appear here</p>
                                </div>
                            </div>
                        )}
                    </motion.div>
                </div>

                {/* Footer */}
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.6, delay: 0.8 }}
                    className="mt-16 text-center text-gray-500 text-sm"
                >
                    <p>⚕️ HealthNexus AI is for informational purposes only. Always consult healthcare professionals for medical advice.</p>
                </motion.div>
            </div>
        </main>
    )
}
