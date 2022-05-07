import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

// import the react routing
import {   
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

// import the react bootstrap elements
import {
    Container,
    Row,
    Col,
    Navbar,
    Nav,
    NavDropdown,
    Image,
    Figure
} from 'react-bootstrap'


// import other react components

import {HomePage} from "./Components/Home" 

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render( 
    <React.StrictMode >
    
        <Navbar bg="light" expand="lg">
        <Container>
            <Navbar.Brand href="/">Logo</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link href="/candidate/browse-jobs">Search Jobs</Nav.Link>
                <Nav.Link href="/employer/browse-companies">Search Companies</Nav.Link>
            </Nav>

            <Nav className="me-auto">
     
                <Nav.Link href="/employer/publish-jobpost">Post a Job</Nav.Link>
                <Nav.Link href="/login">Log In</Nav.Link>
                <Nav.Link href="/register">Register</Nav.Link>
            </Nav>





        </Container>
        </Navbar>

            {/* <main className="d-flex align-items-center ">
                <Container className="main_container">

                    <br/>

                    <Image 
                        src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwellplan.com.my%2Fwp-content%2Fuploads%2F2016%2F09%2FConstruction-Workers.jpg&f=1&nofb=1'
                        className="img-fluid rounded mx-auto d-block"
                        id='home_image_worker'
                    />
                    <br/>
                    <h1 >Jobs, Jobs, Jobs!!! We have plenty of them</h1>
                    <br/>
                    <p>Find jobs near you, and I mean cool jobs, like fireman, cop, welder, trucker, not those boring office jobs these millenials all seem to have</p>
                </Container>

            </main> */}

        


        { /* routes */ } 

            <BrowserRouter > 
            <Routes>
                <Route path="/" element={<HomePage/>}>
                    <Route path="login"></Route>
                    <Route path="register"></Route>
                    <Route path="candidate">
                        <Route path="profile"></Route>
                        <Route path="browse-jobs"></Route>
                        <Route path="retrieve-jobpost"></Route>
                    </Route>
                    <Route path="employer">
                        <Route path="profile"></Route>
                        <Route path="browse-companies"></Route>
                        <Route path="retrieve-job"></Route>
                        <Route path="publish-jobpost"></Route>
                    </Route>
                </Route>
            </Routes>
            </BrowserRouter> 


        { /* end routes */ } 
        
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
