/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    dark: '#16a34a',
                },
                warning: {
                    light: '#fde047',
                    DEFAULT: '#eab308',
                    dark: '#ca8a04',
                },
                danger: {
                    light: '#fca5a5',
                    DEFAULT: '#ef4444',
                    dark: '#dc2626',
                },
            },
            animation: {
                'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'bounce-slow': 'bounce 2s infinite',
            },
        },
    },
    plugins: [],
}
