import axios from 'axios';
import {useState} from 'react';

export const useImageUpload = () => {
    const [fruitName, setName] = useState("");

  const uploadImg = async (img) => {
    const body = new FormData();
    body.append("image", img);
    
    await axios.post('http://192.168.93.33:8000/api/fruit-classifier/',body,{
        headers: {
            Authorization: "Token 90c74bb419419b6d79a56b1534fe084564e9d0a7"
        }
    })
        .then((res) => {
            console.log("inside hook : ",res.data);
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

  return {uploadImg, fruitName};
}