import React, { Component } from "react";

export default class Book extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
      name: "Jonh"
    };
    /* this.handleClick = this.handleClick.bind(this); */
  }
  /* 
  handleClick() {
    console.log("You Clicked ME!");
    console.log(this.state.count);
  } */

  addCount = () => {
    this.setState({ count: this.state.count + 1 });
  };
  resetCount = () => {
    this.setState({ count: (this.state.count = 0) });
  };
  lowerCount = () => {
    this.setState({ count: this.state.count - 1 });
  };

  render() {
    console.log(this.props);

    const { img, title, author } = this.props.info;
    return (
      <article className="book">
        <img src={img} width="150" alt="book"></img>
        <div>
          <h3>Book : {title}</h3>
          <h5>Author : {author}</h5>
          <h3>{this.state.count}</h3>
          <h3>{this.state.name}</h3>
          <button type="button" onClick={this.addCount}>
            Add Contador
          </button>
          <button type="button" onClick={this.resetCount}>
            reset Contador
          </button>
          <button type="button" onClick={this.lowerCount}>
            lower Contador
          </button>
        </div>
      </article>
    );
  }
}
