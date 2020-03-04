import React, { Component } from "react";
import Book from "./Book";
import bookData from "./bookData";
export default class Booklist extends Component {
  /*   state = {
    books: bookData
  };
 */
  constructor(props) {
    super(props);
    this.state = { books: bookData };
  }
  render() {
    /*     const books = this.state.books.map(item => item.book);
    console.log(books); */

    return (
      <section className="booklist">
        {this.state.books.map(item => (
          <Book key={item.id} info={item} />
        ))}
      </section>
    );
  }
}
