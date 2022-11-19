export default function report() {
  return(
    <div className="p-[2rem] w-full cont sm:px-[30%] max-h-[100vh] flex flex-col justify-center items-start">
        <h1 className='w-full px-4 text-main text-[2rem]'>Report Issue</h1>
        <p className='w-full px-4 text-light-Shade'>Help us improve our application!</p>
        <div className="input w-full py-8 flex flex-col gap-6">
            <div className="input_box">
            <input type="text" name='userName'
            required/>
            <span>Username</span>
            <p className='error'>{null}</p>
            </div>
            
            <div className="input_box">
            <textarea cols="30" rows="1"></textarea>
            <span>Mention Issue</span>
            <p className='error'>{null}</p>
            </div>
        </div>
        <button className="px-8 py-2 self-center bg-main hover:scale-[1.05] text-light active:scale-[0.9] rounded-full" type='submit'>SIGNUP</button>
    </div>
)
  }