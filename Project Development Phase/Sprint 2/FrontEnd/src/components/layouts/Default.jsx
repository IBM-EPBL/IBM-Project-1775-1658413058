import Navbar from "../Navbar";

export default function Layout({children}){
    return(
        <>
            <Navbar/>
            {children}
        </>
    )
}