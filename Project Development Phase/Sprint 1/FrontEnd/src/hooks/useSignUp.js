import { useAuthContext } from "./useAuthContext";
import {useState} from 'react';
import axios from "axios";

export const useSignUp = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const { dispatch } = useAuthContext();

    const SignUp = async (userName, password, confPassword) => {
        setIsLoading(true);
        setError(null);

        await axios.post('http://192.168.93.33:8000/api/register-api-user/',{
            username: userName,
            password: password,
            password_2: confPassword
        })
        .then((res) => {
            console.log(res);
            dispatch({type: 'SIGNUP', payload: res.data});
            setIsLoading(false);
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
        })
    };

    return { SignUp, isLoading, error };
}