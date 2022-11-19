import Link from "next/link";

export default function Navbar(){
    
    return(
        <nav className="w-full">
            <div className="w-full text-center py-4">
                <Link href="/" className="text-main no-underline">NUTRA</Link>
            </div>

            <div className="links w-full flex flex-row items-center justify-evenly">
                <Link href="/">Home</Link>
                <Link href="/#about">About</Link>
                <Link href="/report">Report</Link>
                <Link href="/signup">Signup</Link>
            </div>
        </nav>
    )
}