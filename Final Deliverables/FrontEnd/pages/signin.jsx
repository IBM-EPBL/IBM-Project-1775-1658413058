/* eslint-disable */
import AuthPage from "../src/components/layouts/AuthPage";
import Link from "next/link";
import {useState, useEffect} from 'react'
import { useAuthContext } from "../src/hooks/useAuthContext";
import { useRouter } from "next/router";
import axios from "axios";

export default function signin(){
    const router = useRouter();
    const [state, setState] = useState({
        userName: "",
        password: ""
    })
    const [isSignin, setIsSignin] = useState(false)
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState(null);
    const { dispatch } = useAuthContext();

    const handleChange = (e) => {
        setState({
          ...state,
          [e.target.name]: e.target.value 
        })
    }

    const signIn = async () =>{
        setIsLoading(true);
        setError(null);

        await axios.post('http://192.168.61.33:8000/api/user-login',{
            LoginID: state.userName,
            password: state.password
        })
        .then((res) => {
            console.log(res.data.data);
            localStorage.setItem("user", JSON.stringify(res.data.data));
            dispatch({type: 'SIGNIN', payload: res.data.data});
            setIsLoading(false);
            redir();
        })
        .catch((err) => {
            if(err.response){
                setError(err.response.data.error);
            }else if(err.request){
                console.log(err.request);
            }else{
                console.log("Error: ", err.message);
            }
            console.log(err.config);
            setIsLoading(false)
        })
    }

    const redir = () => {
        router.push("/");
    }

    const handleSubmit = () => {
        setIsSignin(true);
    }

    useEffect(() => {
        if(isSignin){
            signIn();
            setIsSignin(false);
        }
    },[isSignin])

    return(
        <div className="p-[2rem] w-full cont sm:px-[30%] min-h-[100vh] flex flex-col justify-center items-start">
            <div className='w-full px-4 flex justify-between items-center flex-row pb-[2rem]'>
                <Link 
                    href="/" className='text-light-Shade text-[0.9rem]'>
                    HOME
                </Link>
                <Link 
                    href="/signup" className='text-light-Shade text-[0.9rem]'>
                    SIGN UP
                </Link>
            </div>
            <h1 className='w-full px-4 text-main text-[2rem]'>Sign in</h1>
            <p className='w-full px-4 text-light-Shade'>Enter your details to continue</p>
            <div className="input w-full py-8 flex flex-col gap-6">
                <div className="input_box">
                <input type="text" name='userName'
                onChange={handleChange}
                required/>
                <span>Username</span>
                </div>
                
                <div className="input_box">
                <input type="password" name='password' 
                onChange={handleChange}
                required/>
                <span>Password</span>
                {error && <p className='error'>{error}</p>}
                </div>
            </div>
            
            <button className={`${isLoading?"pointer-events-none bg-secon":"cursor-pointer bg-main"} px-8 py-2 self-center hover:scale-[1.05] text-light active:scale-[0.9] rounded-full`} onClick={handleSubmit} type='submit'>SIGN IN</button>
        </div>
    )
}

signin.Layout = AuthPage;