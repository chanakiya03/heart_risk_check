import React from 'react';
import HeartForm from './HeartForm';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>❤️ HeartPredict AI</h1>
                <p>Advanced Health Analytics & Decision Support System</p>
            </header>
            <main>
                <HeartForm />
            </main>
            <footer>
                <p>&copy; 2026 HeartPredict AI - Production Ready Medical Assistant</p>
            </footer>
        </div>
    );
}

export default App;
