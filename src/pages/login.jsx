import React from 'react'
import { Link } from 'react-router-dom'

import './login.css'

export default function SignInPage() {
    return (
        <div className="text-center m-5-auto">
            <h2>Sign in</h2>
            <form action="/admin">
                <p>
                    <label>Username or email address</label><br/>
                    <input type="text" name="username" required />
                </p>
                <p>
                    <label>Password</label>
                    <br/>
                    <input type="password" name="password" required />
                </p>
                <p>
                    <button id="sub_btn" type="submit">Login</button>
                </p>
            </form>
            <footer>

            </footer>
        </div>
    )
}