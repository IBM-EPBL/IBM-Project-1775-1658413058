/* eslint-disable */

import { useAuthContext } from "../src/hooks/useAuthContext"
import {useState} from "react"
import axios from 'axios'

export default function report() {
  const { user } = useAuthContext()
  const [message, setMessage] = useState("");
  const [isReport, setIsReport] = useState(false);
  const [name, setName] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const report = async () => {
    setIsLoading(true);
    setError(null);

    await axios.post('http://192.168.61.33:8000/api/report',{
        message: message
    })
    .then((res) => {
        console.log(res.data);
        setIsLoading(false);
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

  const handleChange = (e) => {
    let { value } = e.target;
    if(!value) return;
    setMessage(value);
  }

  const handleClick = ()=>{
    setIsReport(true);
    report();
  }

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
              <textarea className="w-full text-light-Shade outline-none border-none p-[1.5rem] bg-secon rounded-[1rem]" cols="30" rows="5" onChange={handleChange} value={message || ''} placeholder="Enter your issues"></textarea>
              {isReport && <p className="text-green-500">Report sent successfully</p>}
            </div>
            
        </div>
        
        <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" onClick={handleClick} type='submit'>REPORT</button>
    </div>
)
  }