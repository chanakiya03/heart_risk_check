import React, { useState } from 'react';
import axios from 'axios';
import './HeartForm.css';

const API_BASE_URL = "http://127.0.0.1:8000/api";

const fields = [
    { name: "age", label: "Age", type: "number", placeholder: "e.g. 45" },
    { name: "sex", label: "Sex", type: "select", options: [{ v: 1, l: "Male" }, { v: 0, l: "Female" }] },
    { name: "cp", label: "Chest Pain Type", type: "select", options: [
        { v: 0, l: "Typical Angina" }, { v: 1, l: "Atypical Angina" },
        { v: 2, l: "Non-anginal Pain" }, { v: 3, l: "Asymptomatic" }
    ]},
    { name: "trestbps", label: "Resting Blood Pressure", type: "number", placeholder: "e.g. 120" },
    { name: "chol", label: "Serum Cholesterol", type: "number", placeholder: "e.g. 200" },
    { name: "fbs", label: "Fasting Blood Sugar > 120", type: "select", options: [{ v: 1, l: "True" }, { v: 0, l: "False" }] },
    { name: "restecg", label: "Rest ECG", type: "select", options: [
        { v: 0, l: "Normal" }, { v: 1, l: "ST-T Abnormal" }, { v: 2, l: "LV Hypertrophy" }
    ]},
    { name: "thalach", label: "Max Heart Rate", type: "number", placeholder: "e.g. 150" },
    { name: "exang", label: "Exercise Angina", type: "select", options: [{ v: 1, l: "Yes" }, { v: 0, l: "No" }] },
    { name: "oldpeak", label: "ST Depression", type: "number", step: "0.1", placeholder: "e.g. 1.5" },
    { name: "slope", label: "Slope", type: "select", options: [
        { v: 0, l: "Upsloping" }, { v: 1, l: "Flat" }, { v: 2, l: "Downsloping" }
    ]},
    { name: "ca", label: "Major Vessels (0-3)", type: "select", options: [
        { v: 0, l: "0" }, { v: 1, l: "1" }, { v: 2, l: "2" }, { v: 3, l: "3" }
    ]},
    { name: "thal", label: "Thal", type: "select", options: [
        { v: 1, l: "Normal" }, { v: 2, l: "Fixed Defect" }, { v: 3, l: "Reversible Defect" }
    ]}
];

export default function HeartForm() {
    // Initialize form with default values (first option for selects, empty string for inputs)
    const [form, setForm] = useState(
        fields.reduce((acc, f) => ({
            ...acc,
            [f.name]: f.type === "select" ? f.options[0].v : ""
        }), {})
    );

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    // ✅ FIXED: Update state as string to allow typing decimals (e.g. "2.5")
    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        // ✅ FIXED: Convert strings to numbers right before sending
        const payload = {
            ...form,
            age: parseInt(form.age),
            sex: parseInt(form.sex),
            cp: parseInt(form.cp),
            trestbps: parseFloat(form.trestbps),
            chol: parseFloat(form.chol),
            fbs: parseInt(form.fbs),
            restecg: parseInt(form.restecg),
            thalach: parseFloat(form.thalach),
            exang: parseInt(form.exang),
            oldpeak: parseFloat(form.oldpeak),
            slope: parseInt(form.slope),
            ca: parseInt(form.ca),
            thal: parseInt(form.thal),
        };

        try {
            const response = await axios.post(
                `${API_BASE_URL}/predict/`,
                payload,
                { headers: { "Content-Type": "application/json" } }
            );
            setResult(response.data);
        } catch (err) {
            console.error(err);
            setError(err.response?.data?.error || "Server connection failed.");
        } finally {
            setLoading(false);
        }
    };

    const handleRetrain = async () => {
        if (!window.confirm("This will retrain the model with all current database data. Continue?")) return;
        
        setLoading(true);
        try {
            const res = await axios.post(`${API_BASE_URL}/retrain/`);
            alert(`✅ ${res.data.message}`);
        } catch (err) {
            alert("❌ Retrain failed: " + (err.response?.data?.error || err.message));
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="glass-card">
            <h2 className="title">❤️ Heart Health AI</h2>
            
            <form onSubmit={handleSubmit} className="prediction-form">
                <div className="form-grid">
                    {fields.map((f) => (
                        <div key={f.name} className="form-group">
                            <label>{f.label}</label>
                            {f.type === "select" ? (
                                <select 
                                    name={f.name} 
                                    value={form[f.name]} 
                                    onChange={handleChange}
                                    className="input-field"
                                >
                                    {f.options.map(o => (
                                        <option key={o.v} value={o.v}>{o.l}</option>
                                    ))}
                                </select>
                            ) : (
                                <input
                                    type="number"
                                    name={f.name}
                                    value={form[f.name]}
                                    step={f.step || "1"}
                                    placeholder={f.placeholder}
                                    onChange={handleChange}
                                    required
                                    className="input-field"
                                />
                            )}
                        </div>
                    ))}
                </div>

                <div className="button-group">
                    <button type="submit" disabled={loading} className="btn-predict">
                        {loading ? "Analyzing..." : "Predict Risk"}
                    </button>
                    
                    <button 
                        type="button" 
                        onClick={handleRetrain} 
                        disabled={loading} 
                        className="btn-retrain"
                    >
                        🔄 Retrain Model
                    </button>
                </div>
            </form>

            {error && <div className="error-box">{error}</div>}

            {result && (
                <div className={`result-box ${result.risk_level}`}>
                    <h4>Prediction Result</h4>
                    <div className="percentage">{result.risk_percentage}%</div>
                    <div className="level">Risk Level: {result.risk_level}</div>
                </div>
            )}
        </div>
    );
}