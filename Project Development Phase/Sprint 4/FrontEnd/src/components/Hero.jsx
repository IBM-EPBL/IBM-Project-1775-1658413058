import { useAuthContext } from "../hooks/useAuthContext"

export default function Hero () {
    const { user } = useAuthContext();
    const qoutes = ['Go duck yourself ditch']

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
                    <h1 className="text-light text-3xl">Welcome there, <span className="text-main capitalize">{user.userName}</span>!</h1>
                    <p className="text-light-Shade">{qoutes[0]}</p>
                </>
            }
        </div>
    )
}