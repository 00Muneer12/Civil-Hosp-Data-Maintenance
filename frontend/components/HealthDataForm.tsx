'use client'

import { useState, FormEvent } from 'react'
import axios from 'axios'
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

interface HealthDataFormProps {
    onAnalysisComplete: (result: AnalysisResult) => void
    setLoading: (loading: boolean) => void
}

export default function HealthDataForm({ onAnalysisComplete, setLoading }: HealthDataFormProps) {
    const [formData, setFormData] = useState({
        age: '',
        weight: '',
        height: '',
        blood_pressure: '',
        cholesterol_level: '',
        lifestyle_info: '',
    })

    const [errors, setErrors] = useState<Record<string, string>>({})

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target
        setFormData(prev => ({ ...prev, [name]: value }))
        // Clear error when user starts typing
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: '' }))
        }
    }

    const validateForm = () => {
        const newErrors: Record<string, string> = {}

        if (!formData.age || parseInt(formData.age) < 0 || parseInt(formData.age) > 120) {
            newErrors.age = 'Age must be between 0 and 120'
        }
        if (!formData.weight || parseFloat(formData.weight) <= 0) {
            newErrors.weight = 'Weight must be greater than 0'
        }
        if (!formData.height || parseFloat(formData.height) <= 0) {
            newErrors.height = 'Height must be greater than 0'
        }
        if (!formData.blood_pressure || !/^\d{2,3}\/\d{2,3}$/.test(formData.blood_pressure)) {
            newErrors.blood_pressure = 'Blood pressure must be in format 120/80'
        }
        if (!formData.cholesterol_level || parseFloat(formData.cholesterol_level) < 0) {
            newErrors.cholesterol_level = 'Cholesterol level must be positive'
        }
        if (!formData.lifestyle_info || formData.lifestyle_info.length < 10) {
            newErrors.lifestyle_info = 'Please provide detailed lifestyle information'
        }

        setErrors(newErrors)
        return Object.keys(newErrors).length === 0
    }

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()

        if (!validateForm()) {
            return
        }

        setLoading(true)

        try {
            const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
            const response = await axios.post(`${apiUrl}/submit-health-data`, {
                metrics: {
                    age: parseInt(formData.age),
                    weight: parseFloat(formData.weight),
                    height: parseFloat(formData.height),
                    blood_pressure: formData.blood_pressure,
                    cholesterol_level: parseFloat(formData.cholesterol_level),
                    lifestyle_info: formData.lifestyle_info,
                }
            })

            onAnalysisComplete(response.data)
        } catch (error: any) {
            console.error('Error submitting health data:', error)
            alert(error.response?.data?.detail || 'Failed to analyze health data. Please try again.')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="card">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
                <svg className="w-7 h-7 mr-3 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Enter Health Data
            </h2>

            <form onSubmit={handleSubmit} className="space-y-5">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    {/* Age */}
                    <div>
                        <label htmlFor="age" className="label">
                            Age (years) <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="number"
                            id="age"
                            name="age"
                            value={formData.age}
                            onChange={handleChange}
                            className={`input-field ${errors.age ? 'border-red-500' : ''}`}
                            placeholder="e.g., 45"
                        />
                        {errors.age && <p className="text-red-500 text-sm mt-1">{errors.age}</p>}
                    </div>

                    {/* Weight */}
                    <div>
                        <label htmlFor="weight" className="label">
                            Weight (kg) <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="number"
                            step="0.1"
                            id="weight"
                            name="weight"
                            value={formData.weight}
                            onChange={handleChange}
                            className={`input-field ${errors.weight ? 'border-red-500' : ''}`}
                            placeholder="e.g., 75.5"
                        />
                        {errors.weight && <p className="text-red-500 text-sm mt-1">{errors.weight}</p>}
                    </div>

                    {/* Height */}
                    <div>
                        <label htmlFor="height" className="label">
                            Height (cm) <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="number"
                            step="0.1"
                            id="height"
                            name="height"
                            value={formData.height}
                            onChange={handleChange}
                            className={`input-field ${errors.height ? 'border-red-500' : ''}`}
                            placeholder="e.g., 175.0"
                        />
                        {errors.height && <p className="text-red-500 text-sm mt-1">{errors.height}</p>}
                    </div>

                    {/* Blood Pressure */}
                    <div>
                        <label htmlFor="blood_pressure" className="label">
                            Blood Pressure <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="text"
                            id="blood_pressure"
                            name="blood_pressure"
                            value={formData.blood_pressure}
                            onChange={handleChange}
                            className={`input-field ${errors.blood_pressure ? 'border-red-500' : ''}`}
                            placeholder="e.g., 120/80"
                        />
                        {errors.blood_pressure && <p className="text-red-500 text-sm mt-1">{errors.blood_pressure}</p>}
                    </div>
                </div>

                {/* Cholesterol */}
                <div>
                    <label htmlFor="cholesterol_level" className="label">
                        Cholesterol Level (mg/dL) <span className="text-red-500">*</span>
                    </label>
                    <input
                        type="number"
                        step="0.1"
                        id="cholesterol_level"
                        name="cholesterol_level"
                        value={formData.cholesterol_level}
                        onChange={handleChange}
                        className={`input-field ${errors.cholesterol_level ? 'border-red-500' : ''}`}
                        placeholder="e.g., 200.0"
                    />
                    {errors.cholesterol_level && <p className="text-red-500 text-sm mt-1">{errors.cholesterol_level}</p>}
                </div>

                {/* Lifestyle Info */}
                <div>
                    <label htmlFor="lifestyle_info" className="label">
                        Lifestyle Information <span className="text-red-500">*</span>
                    </label>
                    <textarea
                        id="lifestyle_info"
                        name="lifestyle_info"
                        value={formData.lifestyle_info}
                        onChange={handleChange}
                        className={`input-field min-h-[120px] resize-y ${errors.lifestyle_info ? 'border-red-500' : ''}`}
                        placeholder="e.g., Exercise: 3x/week, Smoking: No, Diet: Balanced, Alcohol: Moderate"
                    />
                    {errors.lifestyle_info && <p className="text-red-500 text-sm mt-1">{errors.lifestyle_info}</p>}
                    <p className="text-gray-500 text-xs mt-1">
                        Include: exercise frequency, smoking habits, diet type, alcohol consumption
                    </p>
                </div>

                {/* Submit Button */}
                <motion.button
                    type="submit"
                    className="btn-primary w-full"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                >
                    Analyze Health Data
                </motion.button>
            </form>
        </div>
    )
}
