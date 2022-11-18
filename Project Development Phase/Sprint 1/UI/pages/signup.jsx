/* eslint-disable */
import {useState, useEffect} from 'react'
import { useSignUp } from '../src/hooks/useSignUp';
import Link from 'next/link';

import AuthPage from '../src/components/layouts/AuthPage';

export default function signup() {

  const { SignUp, isLoading, error } = useSignUp();

  const [state, setState] = useState({
    userName: "",
    password: "",
    confPassword: ""
  });
  const [valueError, setValueError] = useState({});
  const [signUp, setSignUp] = useState(false)


  const passCheck = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])[a-zA-Z0-9!@#$%^&*].{7,}$/;

  const validate = ()=>{
    const { password, confPassword} = state;
    const errors = {};
    if(password && !passCheck.test(password)){
      errors.password = "Min-characters: 8, atleast one number and one symbol"
    }
    if(confPassword && confPassword != password){
      errors.confPassword = "Password and confirm password should match"
    }
    setValueError(errors);
  }

  const noValues = () => {
    const {userName, password, confPassword} = state;
    const errors = {};
    if(!userName){
      errors.userName = "User name is required"
    }
    if(!password){
      errors.password = "Password is required"
    }
    if(!confPassword){
      errors.confPassword = "Confirm passwords is required"
    }
    setValueError(errors);
  }

  const handleChange = (e) => {
    setState({
      ...state,
      [e.target.name]: e.target.value 
    })
  }

  const handleSubmit = () => {
    noValues();
    setSignUp(!signUp);
  }

  useEffect(validate,[state]);
  useEffect(() => {
    async () =>{
      if(Object.keys(valueError) === 0){
        console.log("send");
        await SignUp(userName, password, confPassword);
      }
    }
  },[signUp]);

  return (
    <div className="py-[2rem] w-full cont sm:px-[30%] min-h-[100vh] flex flex-col justify-center items-start">
      <div className='w-full px-4 flex justify-between items-center flex-row pb-[2rem]'>
        <Link 
          href="/" className='text-light-Shade text-[0.9rem]'>
            HOME
        </Link>
        <Link 
          href="/signin" className='text-light-Shade text-[0.9rem]'>
            SIGN IN
        </Link>
      </div>
      <h1 className='w-full px-4 text-main text-[2rem]'>Create Account</h1>
      <p className='w-full px-4 text-light-Shade'>Enter your details to register</p>
      <div className="input w-full py-8 flex flex-col gap-6">
        <div className="input_box">
          <input type="text" name='userName' value={state.userName} onChange={handleChange} required/>
          <span>Username</span>
          <p className='error'>{valueError.userName}</p>
        </div>
        
        <div className="input_box">
          <input type="password" name='password' value={state.password} onChange={handleChange} required/>
          <span>Password</span>
          <p className='error'>{valueError.password}</p>
        </div>
        
        <div className="input_box">
          <input type="password" name='confPassword' value={state.confPassword} onChange={handleChange} required/>
          <span>Confirm password</span>
          <p className='error'>{valueError.confPassword}</p>
        </div>
        
      </div>
      <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" type='submit' onClick={handleSubmit} disabled={isLoading}>SIGNUP</button>
      {error && <span className='error'>{error}</span>}
      
    </div>
  )
}

signup.Layout = AuthPage;