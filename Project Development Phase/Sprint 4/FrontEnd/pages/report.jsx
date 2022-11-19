/* eslint-disable */

import { useAuthContext } from "../src/hooks/useAuthContext"
import {useState} from "react"

export default function report() {
  const [isReport, setIsReport] = useState(false);
  const [name, setName] = useState("");

  const handleClick = ()=>{
    setIsReport(true)
  }

  const { user } = useAuthContext();
  return(
    <div className="p-[2rem] w-full cont sm:px-[30%] max-h-[100vh] flex flex-col justify-center items-start">
        <h1 className='w-full px-4 text-main text-[2rem]'>Report Issue</h1>
        <p className='w-full px-4 text-light-Shade'>Help us improve our application!</p>
        <div className="input w-full py-8 flex flex-col gap-6">
            <div className="input_box">
            <input type="text" value={user?user.userName:name} onChange={e=>{setName(e.target.value)}} name='userName'
            required/>
            <span>Username</span>
            <p className='error'>{null}</p>
            </div>
            <span className="px-4 text-light">Mention Issue</span>
            <div className="input_box">
              <textarea className="w-full text-light-Shade outline-none border-none p-[1.5rem] bg-secon rounded-[1rem]" cols="30" rows="5" placeholder="Enter your issues"></textarea>
              {isReport && <p className="text-green-500">Report sent successfully</p>}
            </div>
            
        </div>
        
        <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" onClick={handleClick} type='submit'>REPORT</button>
    </div>
)
  }