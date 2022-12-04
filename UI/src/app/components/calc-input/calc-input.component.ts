import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { fadeIn } from 'animations';
import { ApiService } from 'src/app/api.service';
import { ITextPrediction } from 'src/interfaces/icalc-result';

@Component({
  selector: 'app-calc-input',
  templateUrl: './calc-input.component.html',
  styleUrls: ['./calc-input.component.css'],
  animations: [fadeIn],
})
export class CalcInputComponent implements OnInit {
  textPreds: ITextPrediction[] | undefined;
  inputText: string = '';
  constructor(public router: Router, private apiService: ApiService) {}

  ngOnInit(): void {}
  back() {
    this.router.navigate(['']);
  }
  calc() {
    this.apiService.calc(this.inputText).subscribe({
      next: (res: ITextPrediction[]) => {
        this.textPreds = res;
      },
    });
  }
}
