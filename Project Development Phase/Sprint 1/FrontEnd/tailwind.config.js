/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
         'image-upload': "linear-gradient(90deg, rgba(83,83,83,0.5) 0%, rgba(176,176,176,0.5) 100%), url('../public/bg.jpg')",
      },
      backgroundColor: {
        'prim': "#202124",
        "secon": "#303134",
        "main": "#EC4F1E"
      },
      colors: {
        "light-Shade": "#B3B7BC",
        "light": "#E2E2E2",
        "main": "#EC4F1E"
      }
    },
  },
  plugins: [],
}
