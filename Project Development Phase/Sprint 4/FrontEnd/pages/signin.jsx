/* eslint-disable */
import AuthPage from "../src/components/layouts/AuthPage";
import Link from "next/link";
import {useState, useEffect} from 'react'
import { useAuthContext } from "../src/hooks/useAuthContext";
import { useRouter } from "next/router";

export default function signin(){
    const router = useRouter();
    const [state, setState] = useState({
        userName: "",
        password: ""
    })
    const [isSignin, setIsSignin] = useState(false)
    const [error, setError] = useState(null);
    const { dispatch } = useAuthContext();

    const handleChange = (e) => {
        setState({
          ...state,
          [e.target.name]: e.target.value 
        })
    }

    // const signIn = async () =>{
    //     setIsLoading(true);
    //     setError(null);

    //     await axios.post('http://159.122.174.40:30085/api/register-api-user/',{
    //         username: userName,
    //         password: password
    //     })
    //     .then((res) => {
    //         dispatch({type: 'SIGNIN', payload: res.data});
    //         setIsLoading(false);
    //     })
    //     .catch((err) => {
    //         if(err.response){
    //             setError(err.response.data.error);
    //         }else if(err.request){
    //             console.log(err.request);
    //         }else{
    //             console.log("Error: ", err.message);
    //         }
    //         console.log(err.config);
    //     })
    // }

    const redir = () => {
        router.push("/")
    }

    const handleSubmit = () => {
        dispatch({type: 'SIGNIN', payload: state})
        setIsSignin(true)
    }

    useEffect(() => {
        if(isSignin){
            setIsSignin(false)
            redir();
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
                <p className='error'>{null}</p>
                </div>
                
                <div className="input_box">
                <input type="password" name='password' 
                onChange={handleChange}
                required/>
                <span>Password</span>
                <p className='error'>{null}</p>
                </div>
            </div>
            <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" onClick={handleSubmit} type='submit'>SIGN IN</button>
            {error && <span className='error'>{error}</span>}
        </div>
    )
}

signin.Layout = AuthPage;