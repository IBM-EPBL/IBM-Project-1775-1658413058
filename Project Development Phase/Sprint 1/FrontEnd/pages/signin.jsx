import AuthPage from "../src/components/layouts/AuthPage";
import Link from "next/link";

export default function signin(){
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
            <h1 className='w-full px-4 text-main text-[2rem]'>Create Account</h1>
            <p className='w-full px-4 text-light-Shade'>Enter your details to register</p>
            <div className="input w-full py-8 flex flex-col gap-6">
                <div className="input_box">
                <input type="text" name='userName' required/>
                <span>Username</span>
                <p className='error'>{null}</p>
                </div>
                
                <div className="input_box">
                <input type="password" name='password' required/>
                <span>Password</span>
                <p className='error'>{null}</p>
                </div>
            </div>
            <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" type='submit'>SIGNUP</button>
      
        </div>
    )
}

signin.Layout = AuthPage;