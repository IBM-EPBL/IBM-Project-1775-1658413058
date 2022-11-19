import { useAuthContext } from "../hooks/useAuthContext"

export default function Hero () {
    const { user } = useAuthContext();
<<<<<<< HEAD
    const qoutes = ['All progress takes place outside the confort zone, Your body can stand almost anything it\'s your mind that you have to convince']
=======
    const qoutes = ['Go duck yourself ditch']
>>>>>>> 7d3e3808807bb11c94f101e66332374fb9350eec

    return(
        <div className="cont w-full py-[7rem] rounded-[1rem] bg-secon text-center">
            {!user && 
                <>
                    <h1 className="text-light text-3xl pb-6">AI-Powered Nutrition Analyzer For <span className="text-main capitalize">Fitness Enthusiasts</span></h1>
                    <p className="text-light-Shade">A simple web based application to predict and display the fruit and its nutrition value for fitness enthsiasts.</p>
                </>
            }

            {user && 
                <>
<<<<<<< HEAD
                    <h1 className="text-light pb-6 text-3xl">Welcome there, <span className="text-main capitalize">{user.userName}</span>!</h1>
=======
                    <h1 className="text-light text-3xl">Welcome there, <span className="text-main capitalize">{user.userName}</span>!</h1>
>>>>>>> 7d3e3808807bb11c94f101e66332374fb9350eec
                    <p className="text-light-Shade">{qoutes[0]}</p>
                </>
            }
        </div>
    )
}