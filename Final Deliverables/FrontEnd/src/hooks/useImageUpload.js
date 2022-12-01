import axios from 'axios';
import {useState} from 'react';
import { useAuthContext } from './useAuthContext';

export const useImageUpload = () => {
    const [fruitName, setName] = useState("");
    const { user } = useAuthContext();

  const uploadImg = async (img) => {
    const body = new FormData();
    body.append("image", img);
    
    await axios.post('http://192.168.217.33:8000/api/fruit-classifier/',body,{
        headers: {
            Authorization: `Token ${user.token}`
        }
    })
        .then((res) => {
            setName(res.data.model_predicted_output)
        })
        .catch((err) => {
            if(err.response){
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

  const rmName = () => {setName("")}

  return {uploadImg, fruitName, rmName};
}