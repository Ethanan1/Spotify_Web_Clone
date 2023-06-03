import React, { useState } from 'react';
import './login.css';

function SignupForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSignup = async (e) => {
    e.preventDefault();

    // Perform signup API call using email, password, and confirmPassword
    // Replace the following code with your actual signup API call
    try {
      const response = await fetch('/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
          confirmPassword,
        }),
      });

      if (response.ok) {
        // Successful signup
        console.log('Signup successful');
      } else {
        // Failed signup
        console.error('Signup failed');
      }
    } catch (error) {
      console.error('Error occurred during signup:', error);
    }

    // Reset form fields
    setEmail('');
    setPassword('');
    setConfirmPassword('');
  };

  return (
    <div className="signup-form-container">
      <h2 className="signup-form-heading">Sign Up</h2>
      <form className="signup-form" onSubmit={handleSignup}>
        <div className="signup-form-group">
          <label className="signup-label" htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
            className="signup-input"
          />
        </div>
        <div className="signup-form-group">
          <label className="signup-label" htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
            className="signup-input"
          />
        </div>
        <div className="signup-form-group">
          <label className="signup-label" htmlFor="confirmPassword">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm your password"
            required
            className="signup-input"
          />
        </div>
        <button type="submit" className="signup-button">Sign Up</button>
      </form>
    </div>
  );
}

export default SignupForm;
