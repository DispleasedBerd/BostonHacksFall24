// src/Questionnaire.js
import React, { useState } from "react";

const Questionnaire = ({ onSubmit }) => {
  const [answers, setAnswers] = useState({ question1: "", question2: "" });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAnswers((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(answers);
  };

  return (
    <div>
      <h2>Questionnaire</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>What is your favorite color?</label>
          <input
            type="text"
            name="question1"
            value={answers.question1}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label>What is your favorite animal?</label>
          <input
            type="text"
            name="question2"
            value={answers.question2}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default questionnaire;