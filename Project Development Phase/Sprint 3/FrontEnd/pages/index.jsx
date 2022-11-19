/* eslint-disable */

import Head from 'next/head'
import {Fragment,useRef, useEffect, useState} from 'react'
import { useImageUpload } from '../src/hooks/useImageUpload';
import { Dialog, Transition } from '@headlessui/react';
import axios from 'axios';
import Image from 'next/image';
import { useAuthContext } from '../src/hooks/useAuthContext';
import Hero from '../src/components/Hero';
import Link from 'next/link';

export default function Home() {
  const imgFile = useRef();

  const { user } = useAuthContext();

  const [imgUrl, setImgUrl] = useState("/bg.jpg")

  const [searchInp, setSearchInp] = useState("")
  const {uploadImg, fruitName, setName} = useImageUpload();
  const [search, setSearch] = useState("");
  const [fruitId, setFruitId] = useState("");
  const [isSearch, setIsSearch] = useState(false);
  const [isOpen , setIsOpen] = useState(false);
  const [isSearchImg, setIsSearchImg] = useState(false);
  const [nutri, setNutri] = useState(null)

  const fetchNutriValue = async () => {
    await axios.get(`http://159.122.174.40:30085/api/calorie-detail/${fruitId}`)
        .then((res) => {
            setNutri(res.data);
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
  }

  const searchId = async () => {
    await axios.get(`http://159.122.174.40:30085/api/search-fruits/?ordering=-id&search=${search}`)
        .then((res) => {
            setFruitId(res.data.results[0].id)
            setIsSearch(true)
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
  }

  const handleSearch = () => {
    searchId();
  }

  const closeModal = () => {
    setIsOpen(false)
  }

  const handleClick = () => {
    // uploadImg(imgFile.current.files[0]);
    setSearch("APPLE")
    setIsSearchImg(true)
  }

  useEffect(()=>{
    if(isSearchImg){
      searchId()
      setIsSearchImg(false)
    }
  },[isSearchImg])

  useEffect(() => {
    if(isSearch){
      fetchNutriValue()
      setIsSearch(false)
    }
  },[isSearch])

  useEffect(()=>{
    if(nutri){
      setIsOpen(true)
    }
  },[nutri]);

  useEffect(()=>{
    setName("")
  },[fruitName]);

  const handleImg = () => {
    const iFile = imgFile.current.files[0]
    if(iFile){
      setImgUrl(URL.createObjectURL(iFile))
    }
  }

  return (
    <div className="w-full relative cont">
      <Head>
        <title>Nutra</title>
        <meta name="description" content="Generated by create next app" />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>
      
      <div 
      className='search py-[1rem] flex flex-row items-center justify-center gap-[0.3rem] w-full'>

        <input 
        className='rounded-[5rem] px-[1rem] py-[0.6rem] outline-none bg-secon text-light-Shade' 
        type="text" 
        value={searchInp}
        onChange={e => {setSearch(e.target.value); setSearchInp(e.target.value)}}
        placeholder='Enter fruit name' 
        />

        <button 
        className='rounded-[5rem] bg-main py-[0.6rem] text-light px-[1.5rem] active:scale-90'
        onClick={handleSearch}
        >search</button>
      </div>

      <Hero/>

      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={closeModal}>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>

          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-secon p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title
                    as="h3"
                    className="py-2 text-2xl font-medium leading-6 capitalize text-light"
                  >
                    {search}
                  </Dialog.Title>
                  <div className="py-4">
                    <p className="text-light-Shade text-lg text-secon">
                      Calories: <span className="text-main text-sm text-">{nutri && nutri.calories}</span>
                    </p>
                    <p className="text-light-Shade text-lg text-secon">
                      Carbohydrate: <span className="text-sm text-main">{nutri && nutri.carbohydrate_value}</span>
                    </p>
                    <p className="text-light-Shade text-lg text-secon">
                      Protien: <span className="text-main text-sm text-secon">{nutri && nutri.protein_value}</span>
                    </p>
                    <p className="text-light-Shade text-lg text-secon">
                      Fat: <span className="text-main text-sm text-secon">{nutri && nutri.fat_value}</span>
                    </p>
                  </div>

                  <div className="mt-4">
                    <button
                      type="button"
                      className="inline-flex justify-center rounded-full border border-transparent bg-main px-4 py-2 text-sm font-medium text-light hover:bg-prim
                      active:scale-90
                      focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                      onClick={closeModal}
                    >
                      Got it
                    </button>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>

      {!user && 
        <div className="w-full my-4 px-6 py-8 bg-secon rounded-[1rem]">
          <h1 className="text-main text-xl pb-4">Join Us</h1>
          <p className="text-light-Shade pb-8">Inorder to use our AI based analyzer please register. We have implemented a CNN based model to predict and analyze the nutrition values of fruits using image.</p>
          <Link className='rounded-full text-main border border-main py-[0.5rem] px-[1rem]' href="/signup">Join Us</Link>
        </div>
      }

      {user && 
        <div className="w-full my-4 p-6 bg-secon rounded-[1rem]">
          <h1 className="text-main text-xl pb-8">Upload fruit image</h1>
          <div className="w-full h-full flex  items-center flex-col sm:flex-row justify-evenly ">
            <Image src={imgUrl} width="320" height="320" alt='image'/>
            <div className="flex pt-4 flex-row sm:flex-col gap-[1rem]">
              <label className='bg-prim text-light-Shade px-[1.5rem] rounded-full py-[0.6rem]' htmlFor="img">Select Image</label>
              <input className='hidden' id='img' type="file" onChange={handleImg} ref={imgFile}/>
              <button className='bg-prim text-light-Shade px-[1.5rem] rounded-full py-[0.6rem] grow-0' type="submit" onClick={handleClick}>Upload</button>
            </div>
          </div>
        </div>
      }

      <div id='about' className="w-full my-4 px-6 py-8 rounded-[1rem] bg-secon">
        <h1 className="text-main text-xl pb-4">About</h1>
        <p className="text-light-Shade">
          Nutrition analyzer aims to use personal information about individuals
          or groups of individuals to deliver nutritional advice that, theoretically, would
          be more suitable than generic advice. Nutritional analysis is the process of
          determining the nutritional content of food. Deep learning, a sub branch of
          Artificial Intelligence, has promised to aid in the development of predictive
          models that are suitable for analyzing Nutrition. Using the prediction made
          by CNN to provide nutrition values of the food or fruits, that help fitness
          enthusiasts to track their daily nutrition intake to maintain a healthy life.
        </p>
      </div>
      
    </div>
  )
}
