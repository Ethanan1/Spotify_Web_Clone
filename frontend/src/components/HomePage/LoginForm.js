import React, { useState } from 'react';
import './login.css';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    // Perform login API call using email and password
    // Replace the following code with your actual login API call
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
        }),
      });

      if (response.ok) {
        // Successful login
        console.log('Login successful');
      } else {
        // Failed login
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
    }

    // Reset form fields
    setEmail('');
    setPassword('');
  };

  return (
    <div className="login-form-container">
      <h2 className="login-form-heading">Login</h2>
      <form className="login-form" onSubmit={handleLogin}>
        <div className="login-form-group">
          <label className="login-label" htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
            className="login-input"
          />
        </div>
        <div className="login-form-group">
          <label className="login-label" htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
            className="login-input"
          />
        </div>
        <button type="submit" className="login-button">Login</button>
      </form>
    </div>
  );
}

export default LoginForm;
