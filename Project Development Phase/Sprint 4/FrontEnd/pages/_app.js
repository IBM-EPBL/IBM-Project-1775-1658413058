import Default from '../src/components/layouts/Default.jsx'
import { AuthContextProvider } from '../src/context/authContext'
import '../styles/globals.css'
import '../styles/signup.scss'
import '../styles/navbar.scss'



function MyApp({ Component, pageProps }) {

  const Layout = Component.Layout || Default;

  return (
      <AuthContextProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </AuthContextProvider>
  )
}

export default MyApp
