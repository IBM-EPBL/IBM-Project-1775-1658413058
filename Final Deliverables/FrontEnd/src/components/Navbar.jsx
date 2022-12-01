import Link from "next/link";
import { useAuthContext } from "../hooks/useAuthContext";

export default function Navbar(){
    const { user, dispatch } = useAuthContext();

    return(
        <nav className="cont w-full">
            <div className="w-full text-center py-4">
                <Link href="/" className="text-main no-underline">NUTRA</Link>
            </div>

            <div className="links w-full pb-4 flex flex-row sticky top-0 items-center justify-evenly">
                <Link href="/">Home</Link>
                <Link href="#about">About</Link>
                <Link href="/report">Report</Link>
                {!user && <Link href="/signin">Signin</Link>}
                {user && <button className="py-[0.2rem] text-main px-[1rem] border rounded-full border-main" onClick={() => {dispatch({type: 'SIGNOUT'});localStorage.removeItem('user')}}>Log out</button>}
            </div>
        </nav>
    )
}