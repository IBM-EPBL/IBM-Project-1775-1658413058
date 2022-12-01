import { useAuthContext } from "./useAuthContext";
import {useState} from 'react';
import axios from "axios";
import { useRouter } from "next/router";

export const useSignUp = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const { dispatch } = useAuthContext();
    const router = useRouter();

    const SignUp = async (userName, password, confPassword) => {
        setIsLoading(true);
        setError(null);

        await axios.post('http://159.122.174.40:31738/api/register-api-user/',{
            username: userName,
            email: "test@gmail.com",
            password: password,
            password_2: confPassword
        })
        .then((res) => {
            localStorage.setItem("user", JSON.stringify(res.data));
            dispatch({type: 'SIGNUP', payload: res.data});
            setIsLoading(false);
            router.push("/");
        })
        .catch((err) => {
            if(err.response){
                setError(err.response.data.error);
                console.log(err.response.data);
                console.log(err.response.status);
                console.log(err.response.headers);
            }else if(err.request){
                console.log(err.request);
            }else{
                console.log("Error: ", err.message);
            }
            console.log(err.config);
            setIsLoading(false)
        })
    };

    return { SignUp, isLoading, error };
}