import './App.css'
import * as React from "react";
import Cookies from "universal-cookie";

const cookies = new Cookies();

interface LoginProps {
    email: string;
    password: string;
    error: string;
    isAuthenticated: boolean;
}


class App extends React.Component<any,LoginProps> {


  constructor(props: any) {
    super(props);

    this.state = {
      email: this.props.email,
      password: this.props.password,
      error: this.props.error,
      isAuthenticated: this.props.isAuthenticated,
    };
  }

  componentDidMount = () => {
    this.getSession();
  };
  handlePasswordChange = (event:any) => {
    this.setState({password: event.target.value});
  };

  handleUserNameChange = (event:any) => {
    this.setState({email: event.target.value});
  };

  isResponseOk(response: Response) {
      console.log('response',response);
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  getSession = () => {
    fetch("/_accounts/browser/v1/auth/session", {
      credentials: "same-origin",
    })
    .then((res: Response): Promise<any> => res.json())
    .then((data) => {
      console.log(data);

      this.setState({isAuthenticated: data.isAuthenticated});

    })
    .catch((err) => {
      console.log(err);
    });
  };


  login = (event:any) => {
    event.preventDefault();
    fetch("/_accounts/browser/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get("csrftoken"),
      },
      credentials: "same-origin",
      body: JSON.stringify({email: this.state.email, password: this.state.password}),
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: true, email: "", password: "", error: ""});
    })
    .catch((err) => {
      console.log(err);
      this.setState({error: "Wrong email or password."});
    });
  };


  logout = () => {
    fetch("/_accounts/browser/v1/auth/session", {
      method: "DELETE",
      credentials: "same-origin",
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: false});
    })
    .catch((err) => {
      console.log(err);
    });
  };

   render() {
    if (!this.state.isAuthenticated) {
      return (
        <div className="container mt-3">
          <h1>React Cookie Auth</h1>
          <br />
          <h2>Login</h2>
          <form onSubmit={this.login}>
            <div className="form-group">
              <label htmlFor="email">Username</label>
              <input type="text" className="form-control" id="email" name="email" value={this.state.email} onChange={this.handleUserNameChange} />
            </div>
            <div className="form-group">
              <label htmlFor="email">Password</label>
              <input type="password" className="form-control" id="password" name="password" value={this.state.password} onChange={this.handlePasswordChange} />
              <div>
                {this.state.error &&
                  <small className="text-danger">
                    {this.state.error}
                  </small>
                }
              </div>
            </div>
            <button type="submit" className="btn btn-primary">Login</button>
          </form>
        </div>
      );
    }
    return (
      <div className="container mt-3">
        <h1>React Cookie Auth</h1>
        <p>You are logged in!</p>
        {/*<button className="btn btn-primary mr-2" onClick={this.whoami}>WhoAmI</button>*/}
        <button className="btn btn-danger" onClick={this.logout}>Log out</button>
      </div>
    )
  }
}

export default App
