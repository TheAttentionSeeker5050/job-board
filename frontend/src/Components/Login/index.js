import React from 'react';
import './index.css';



// import the react bootstrap elements
import {
    Container,
    Row,
    Col,
    Image,
    Figure, 
    Form,
    Button, 
} from 'react-bootstrap'

export class LoginPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            username:"",
            password:""
        }

        // for handling the form data
        this.handlePassword = this.handlePassword.bind(this)
        this.handleUsername = this.handleUsername.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        // this.handleChange = this.handleChange.bind()

    }

    handleUsername(event) {
        // for handling and storing input data

        this.setState({
            username: event.target.value
        })
    }

    handlePassword(event) {
        // for handling and storing input data
        this.setState({
            password: event.target.value
        })
    }



    handleSubmit(event) {
        // for sumbitting the form login data
        // we will add more data validaton later on
        if (this.state.username != "" && this.state.password != "") {
            // alert("a username and password was submitted" + this.state.username + " " + this.state.password)
            this.APICall(this.state.username, this.state.password)
        } else {
            console.log("api call failed")
        }
        event.preventDefault()

    }

    APICall (){
        // we use this funciton to make an api call to the backend for 
        // requesting the authentication token 

        let user = {
            username: this.state.username,
            password: this.state.password
        }



        fetch("http://localhost:8000/api/token/obtain/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        })
            .then(response => response.json())
            .then(data => {
                localStorage.setItem("access_token", data.access)
                localStorage.setItem("refresh_token", data.refresh)

            })
            .catch(error => {
                console.error("Error: \n", error)
            })
    }

    render () {
        return (
            <Container className='login_register_container'>
                <Form onSubmit={this.handleSubmit}>
                    <h1>Log in</h1>
                    <Form.Group className='mb-3' controlId='formBasicUsername'>
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control
                            name="username" type='username' placeholder='Enter email'
                            value={this.state.username} onChange={this.handleUsername}/>
                    </Form.Group>

                    <Form.Group className='mb-3' controlId='formBasicPassword'>
                        <Form.Label>Password</Form.Label>
                        <Form.Control 
                        name='password' type='password' placeholder='Enter password'
                        value={this.state.password} onChange={this.handlePassword}/>
                    </Form.Group>

                    <Button onSubmit={this.handleSubmit} type='submit'>Log In</Button>
                    {/* <input className="btn btn-primary mb-3" type="submit" value="Log in"/> */}


                </Form>
            </Container>
        )
    }
}