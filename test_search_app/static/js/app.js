window.ee = new EventEmitter();

var btnClickDate;

var Measure = React.createClass({
    getInitialState: function () {
        return {
            elapsedTime: null,
            booksLength: 0
        };
    },
    componentDidMount: function () {
        var self = this;
        window.ee.addListener('Measure.update', function (data) {
            self.setState(
                {
                    elapsedTime: data.time,
                    booksLength: data.length
                });
        });
    },
    componentWillUnmount: function () {
        window.ee.removeListener('Measure.update');
    },
    render: function () {
        var booksLength = this.state.booksLength;
        var elapsedTime = this.state.elapsedTime;
        var elapsedTimeSec;
        if (elapsedTime === null) {
            elapsedTimeSec = null
        }
        else {
            elapsedTimeSec = (this.state.elapsedTime / 1000).toFixed(2)
        }
        return (
            <div>
                <p className={elapsedTime === null ? 'none': 'measured_data'}>
                    Found: {booksLength} ({elapsedTimeSec} s)
                </p>
            </div>)
    }
});


var Keywords = React.createClass({
    propTypes: {
        words: React.PropTypes.array.isRequired
    },
    render: function () {
        var words = this.props.words;
        return (
            <p>
                {words.map(function (word, index) {
                    return (
                        <span key={index} className={word.is_matching == true ? '':'line_through'}>{word.word} </span>
                    )
                })
                }
            </p>
        )
    }
});


var Book = React.createClass({
    propTypes: {
        book: React.PropTypes.shape({
            id: React.PropTypes.string.isRequired,
            title: React.PropTypes.string.isRequired,
            score: React.PropTypes.number.isRequired,
            words: React.PropTypes.array.isRequired
        })
    },

    render: function () {
        var id = this.props.book.id,
            title = this.props.book.title,
            score = this.props.book.score,
            key = this.props.key,
            words = this.props.book.words;


        return (
            <tr key={key}>
                <td>{id}:</td>
                <td>{title}</td>
                <td>{score}</td>
                <td><Keywords words={words}/></td>
            </tr>
        )
    }
});


var Results = React.createClass({
    propTypes: {
        books: React.PropTypes.array.isRequired
    },
    componentDidUpdate: function () {
        var books = this.props.books;
        if (books.length != 0) {
            var time = new Date() - btnClickDate;
            window.ee.emit('Measure.update', {'time': time, 'length': books.length});
        } else {
            window.ee.emit('Measure.update', {'time': null, 'length': 0})
        }
    },
    render: function () {
        var books = this.props.books;
        var resultsTemplate;

        if (books.length > 0) {
            resultsTemplate = (
                <table className="table table-hover table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Score</th>
                        <th>Keywords</th>
                    </tr>
                    </thead>
                    <tbody>
                    {books.map(function (item, index) {
                        return (
                            <Book book={item} key={index}/>
                        )
                    })
                    }
                    </tbody>
                </table>)
        } else if (btnClickDate !== undefined) {
            resultsTemplate = <p className="not_found_msg">No matching records found</p>
        }
        return (
            <div className='results'>
                {resultsTemplate}
            </div>
        );
    }
});


var Search = React.createClass({
    getInitialState: function () {
        return {
            queryIsEmpty: true,
            success: true,
            exception: ''
        };
    },
    onQueryChange: function (e) {
        if (e.target.value.trim().length > 0) {
            this.setState({queryIsEmpty: false})
        } else {
            this.setState({queryIsEmpty: true})
        }
    },

    handleKeyPress: function (event) {
        if (event.charCode == 13 && this.state.queryIsEmpty == false) {
            document.getElementById('btnSearch').click();
        }
    },
    onBtnClickHandler: function (e) {
        e.preventDefault();
        var query = ReactDOM.findDOMNode(this.refs.query).value;
        btnClickDate = new Date();

        var self = this;
        $.ajax({
            type: 'GET',
            url: '/search/',
            data: {
                query: query
            },
            success: function (data) {
                if (data.success == true) {
                    self.setState({
                        success: true,
                        exception: ''
                    });
                    window.ee.emit('Results.update', data);
                } else {
                    self.setState({
                        success: false,
                        exception: data.exception
                    })
                }
            }
        });
    },
    render: function () {
        var queryIsEmpty = this.state.queryIsEmpty,
            success = this.state.success,
            exception = this.state.exception;
        return (
            <div>
                <div className="input-group">
                    <input type="text"
                           className="form-control"
                           placeholder="Search for..."
                           onChange={this.onQueryChange}
                           ref='query'
                           onKeyPress={this.handleKeyPress}
                           maxLength = "512"
                    />
            <span className="input-group-btn">
                <button className="btn btn-default"
                        type="button"
                        onClick={this.onBtnClickHandler}
                        ref='search_button'
                        id="btnSearch"
                        disabled={queryIsEmpty}
                >Search</button>
            </span>
                </div>
                <p className={success == true ? 'none': 'alert alert-danger'}>Exception: {exception}</p>
            </div>
        );

    }
});


var App = React.createClass({
    getInitialState: function () {
        return {
            books: []
        };
    },
    componentDidMount: function () {
        var self = this;
        window.ee.addListener('Results.update', function (results) {
            self.setState(
                {
                    books: results.data.results
                });
        });
    },
    componentWillUnmount: function () {
        window.ee.removeListener('Results.update');
    },
    render: function () {
        return (
            <div className='app'>
                <Search />
                <Measure />
                <Results books={this.state.books}/>
            </div>
        );
    }
});

ReactDOM.render(
    <App />,
    document.getElementById('root')
);